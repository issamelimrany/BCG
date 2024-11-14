const express = require('express');
hello  = require('../controllers/hello');
router = express.Router();
hello= require('../controllers/hello') 

router.get('/',hello.hello);


module.exports = router;