const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

// Product list
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Create Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to get an item by ID
const getItemById = (id) => listProducts.find((product) => product.itemId === id);

// Function to reserve stock by ID
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Function to get the current reserved stock by ID
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock, 10) : null;
};

// Route to get the list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get a product by ID and its current stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  product.currentQuantity = currentStock !== null ? currentStock : product.initialAvailableQuantity;
  res.json(product);
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock = currentStock !== null ? currentStock : product.initialAvailableQuantity;
  if (availableStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, availableStock - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});