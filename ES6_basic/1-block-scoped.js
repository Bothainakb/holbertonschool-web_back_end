export default function taskBlock(trueOrFalse) {
  let task = false;
  const task2 = true;

  if (trueOrFalse) {
    task = true;
    // task2 remains true
  }

  return [task, task2];
}
