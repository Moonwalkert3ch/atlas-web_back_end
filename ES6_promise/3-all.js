import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise
    .all([uploadPhoto(), createUser()])
    .then((resolve) => {
      console.log(`${resolve[0].body} ${resolve[1].firstName} ${rsolve[1].lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
