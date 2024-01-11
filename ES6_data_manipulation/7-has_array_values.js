// function that returns t/f if element exist in array
export default function hasValuesFromArray(set, array) {
  // return results if element exists in the array
  return array.every((elements) => set.has(elements));
}
