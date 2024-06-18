const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

router.get('/', AppController.getHome);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:majorto', StudentsController.getAllStudentsByMajor);

module.exports = router;
