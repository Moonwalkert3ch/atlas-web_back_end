// function thtat returns a new arraybiffer with int8 value

export default function createInt8TypedArray(length, position, value) {
  const int8View = new DataView(new ArrayBuffer(length));

  // try setting the value at int8array position
  try {
    int8View.setInt8(position, value);
  } catch (error) {
    // handles error
    throw new Error('Position outside range');
  }

  // return new arraybuffer
  return int8View;
}
