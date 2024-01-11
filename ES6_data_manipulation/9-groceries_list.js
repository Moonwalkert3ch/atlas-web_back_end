// function that returns  a map of groceries
export default function groceriesList() {
  // create a grocery list
  const groceryItems = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];

  // return a map of grocery list
  return new Map(groceryItems);
}
