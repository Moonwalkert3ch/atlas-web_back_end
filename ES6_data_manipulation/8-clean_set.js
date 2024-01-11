// function that returns a string of all set values that start with
export default function cleanSet(set, startString) {
  // set to store set values
  const cleanedSet = new Set();

  // check if set is valid and startString is string
  if (!(set instanceof Set) || typeof startString !== 'string') {
    // returns empty string if not true
    return '';
  }

  // loop through the set values
  for (const value of set.values()) {
    // check for string
    if (typeof value === 'string' && value.startsWith(startString)) {
      // remove the substring after startString value
      const newStringValue = value.substring(startString.length);

      // check for newStringValue
      if (newStringValue !== value) {
        // concatenate newStringValue to the set values storage
        cleanedSet.add(newStringValue);
      }
    }
  }

  // convert set and seperate with -
  return Array.from(cleanedSet).join('-');
}
