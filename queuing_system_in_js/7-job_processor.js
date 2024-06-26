import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Track job progress

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100); // Track job progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process jobs from the queue 'push_notification_code_2' with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Listen for job events
queue.on('job complete', (id, result) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    job.remove((err) => {
      if (err) throw err;
      console.log(`Notification job ${job.id} completed`);
    });
  });
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Notification job ${id} failed: ${errorMessage}`);
});

queue.on('job progress', (id, progress) => {
  console.log(`Notification job ${id} ${progress}% complete`);
});
