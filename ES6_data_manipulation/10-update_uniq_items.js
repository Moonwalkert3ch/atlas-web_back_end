// function that returns a map for items w qty of 1
export default function updateUniqueItems(map) {
  // check for arg map is a valid Map
  if (!(map instanceof Map)) {
    // throw error Map isnt valid
    throw new Error('Cannot process');
  }

  // loop through map entries
  for (const [uniqueItem, quantity] of map.entries()) {
    // check if the quantity is 1
    if (quantity === 1) {
      // update the quantity to 100
      map.set(uniqueItem, 100);
    }
  }

  // return updated map
  return map;
}
