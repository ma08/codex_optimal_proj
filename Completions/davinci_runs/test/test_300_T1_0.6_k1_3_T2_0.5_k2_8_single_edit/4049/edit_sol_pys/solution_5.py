// Array of objects
var people = [
  {
    name: 'John Doe',
    age: 30,
    gender: 'male'
  },
  {
    name: 'Jane Doe',
    age: 25,
    gender: 'female'
  },
  {
    name: 'Steven Smith',
    age: 32,
    gender: 'male'
  },
  {
    name: 'Stacy Williams',
    age: 21,
    gender: 'female'
  }
];

// Loop through array
for (var i = 0; i < people.length; i++) {
  // Create new div element
  var div = document.createElement('div');
  // Assign class attribute
  div.setAttribute('class', 'person');
  // Add text node with person's name
  div.appendChild(document.createTextNode(people[i].name));
  // Add div element to DOM
  document.getElementById('people').appendChild(div);
}
