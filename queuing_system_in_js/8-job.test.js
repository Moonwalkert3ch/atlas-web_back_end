import { expect } from "chai";
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should give an error message if jobs not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    });

    it('should create new job to the queue', () => {
        const jobs = [
            {
                phoneNumber: '123456789',
                message: 'This is the code 1234 to verify your account'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(1);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    });

    it('should give message on job events', () => {
        const jobs = [
            {
                phoneNumber: '123456789',
                message: 'This is the code 1234 to verify your account'
            }
        ];

        const consoleSpy = sinon.spy(console, 'log');
        createPushNotificationsJobs(jobs, queue);
        const job = queue.testMode.jobs[0];

        job.id = 1;

        job._events.complete();
        expect(consoleSpy.calledWith(`Notification job ${job.id} completed`)).to.be.true;

        job._events.failed('Some error');
        expect(consoleSpy.calledWith(`Notification job ${job.id} failed: Some error`)).to.be.true;
    
        job._events.progress(50);
        expect(consoleSpy.calledWith(`Notification job ${job.id} 50% complete`)).to.be.true;
    
        consoleSpy.restore();
    });
});
