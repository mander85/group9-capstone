const fs = require('fs');

const courses = JSON.parse(
  fs.readFileSync(`${__dirname}/../dev-data/data/loan.json`)
);

// SELECT ( Get) - READ Request Handlers
exports.getAllcourses = (req, res) => {
  console.log(req.requestTime);

  res.status(200).json({
    status: 'success',
    requestedAt: req.requestTime,
    results: courses.length,
    data: {
      courses
    }
  });
};

exports.getcourse = (req, res) => {
  console.log(req.params);
  const id = req.params.id * 1;

  const course = courses.find(el => el.id === id);

  res.status(200).json({
    status: 'success',
    data: {
      course
    }
  });
};
// INSERT( Post) - CREATE Request Handler

exports.createcourse = (req, res) => {
  // console.log(req.body);

  const newId = courses[courses.length - 1].id + 1;
  const newcourse = Object.assign({ id: newId }, req.body);

  courses.push(newcourse);

  fs.writeFile(
    `${__dirname}/dev-data/data/loan.json`,
    JSON.stringify(courses),
    err => {
      res.status(201).json({
        status: 'success',
        data: {
          course: newcourse
        }
      });
    }
  );
};
// UPDATE (Update)
exports.updatecourse = (req, res) => {
  res.status(200).json({
    status: 'success',
    data: {
      course: '<Updated course here...>'
    }
  });
};

// DELETE (Delete) Request Handler
exports.deletecourse = (req, res) => {
  res.status(204).json({
    status: 'success',
    data: null
  });
};
