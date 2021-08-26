const apiGet = async (url) => {
  //   let headers = new Headers();

  //   headers.append('Content-Type', 'application/json');
  //   headers.append('Accept', 'application/json');
  //   headers.append('Origin', 'http://localhost:8000');
  try {
    const response = await axios.get(url);
    // , {
    //   headers: headers,
    // });
    body = document.querySelector('#container');
    html = `<table style="width:50%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Number</th>
      </tr>
      `;
    response.data.forEach((element) => {
      line = `      
          <tr>
              <td>${element.first_name}</td>
              <td>${element.last_name}</td>
              <td>${element.number}</td>
          </tr>`;
      html += line;
    });
    html += '</table>';
    body.innerHTML = html;
  } catch (err) {
    console.log(err.message);
  }
};

const apiPost = async (url, data) => {
  try {
    const response = await axios.post(url, data);
    // , {
    //   headers: headers,
    // });
    body = document.querySelector('#message');

    body.innerHTML = response.data.message;
  } catch (err) {
    console.log(err.message);
  }
};

apiGet('http://localhost:8000/api/student/');
// apiPost('http://localhost:8000/api/student/', {
//   first_name: 'veysel',
//   last_name: 'veysel',
//   number: 1002,
// });

let form = document.getElementById('form'); // selecting the form

form.addEventListener('submit', async function (event) {
  // 1
  event.preventDefault();
  console.log('form submit');

  let data = new FormData(); // 2

  data.append('first_name', document.getElementById('name').value);
  data.append('last_name', document.getElementById('lastname').value);
  data.append('number', document.getElementById('number').value); // 3

  try {
    const response = await axios.post(
      'http://localhost:8000/api/student/',
      data
    );

    body = document.querySelector('#message');

    body.innerHTML = response.data.message;
    apiGet('http://localhost:8000/api/student/');
    document.getElementById('name').value = '';
    document.getElementById('lastname').value = '';
    document.getElementById('number').value = '';
  } catch (err) {
    console.log(err.message);
  }

  //   axios
  //     .post('http://localhost:8000/api/student/', data) // 4
  //     .then((res) => alert('Form Submitted')) // 5
  //     .catch((errors) => console.log(errors)); // 6
});
