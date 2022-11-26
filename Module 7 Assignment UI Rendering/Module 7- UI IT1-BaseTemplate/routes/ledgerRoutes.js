const express = require('express');
const ledgerController= require('../controllers/ledgerController');

const router = express.Router();

router
  .route('/')
  .get(ledgerController.getAllUsers)
  .post(ledgerController.createUser);

router
  .route('/:id')
  .get(ledgerController.getUser)
  .patch(ledgerController.updateUser)
  .delete(ledgerController.deleteUser);

module.exports = router;