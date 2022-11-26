const express = require('express');
const loanController= require('../controllers/loanController');

const router = express.Router();

router
  .route('/')
  .get(loanController.getAllUsers)
  .post(loanController.createUser);

router
  .route('/:id')
  .get(loanController.getUser)
  .patch(loanController.updateUser)
  .delete(loanController.deleteUser);

module.exports = router;