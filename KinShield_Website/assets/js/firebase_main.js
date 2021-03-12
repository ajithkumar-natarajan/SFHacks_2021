'use strict';

//grab a form
const form = document.querySelector('.form-inline');

//grab an input
const inputFullName = form.querySelector('#inputFullName');
const inputAge = form.querySelector('#inputAge');
const inputEmail = form.querySelector('#inputEmail');
const inputKid = form.querySelector('#inputKidTrue');
const inputZip = form.querySelector('#inputZip');

// console.log(inputFullName);
// console.log(inputAge);
// console.log(inputEmail);
// console.log(inputKid);
// console.log(inputZip);


//config your firebase push
const config = {
    apiKey: "AIzaSyC3Il9b0FniBq1tOcsCFLT472YBhEDNIFw",
    authDomain: "kinshield-875de.firebaseapp.com",
    databaseURL: "https://kinshield-875de-default-rtdb.firebaseio.com",
    projectId: "kinshield-875de",
    storageBucket: "kinshield-875de.appspot.com",
    messagingSenderId: "983899426671"
};


//create a functions to push
    function firebasePush(input) {
        if (!firebase.apps.length) {
            firebase.initializeApp(config);
        }

        var mailsRef = firebase.database().ref('message').push().set(
            {
                // name: input.value
                name: input[0],
                age: parseInt(input[1]),
                email: input[2],
                kid: input[3] == "true",
                zip: parseInt(input[4])
            }
        );

    }

//push on form submit
    if (form) {
        form.addEventListener('submit', function (evt) {
            evt.preventDefault();

            //prevents from braking
            // if (!firebase.apps.length) {
            //     firebase.initializeApp(config);
            // }

            let arr = new Array(inputFullName.value, inputAge.value, inputEmail.value, inputKid.value, inputZip.value);
            firebasePush(arr);
            // firebasePush(inputFullName);
            //push itself
            // var mailsRef = firebase.database().ref('webapp').push().set(
            //     {
            //         name: input.value
            //     }
            // );
            // firebasePush(inputAge);
            //push itself
            // var mailsRef = firebase.database().ref('webapp').push().set(
            //     {
            //         age: input.value
            //     }
            // );
            // firebasePush(inputEmail);
            //push itself
            // var mailsRef = firebase.database().ref('webapp').push().set(
            //     {
            //         email: input.value
            //     }
            // );
            // firebasePush(inputKidTrue);
            //push itself
            // var mailsRef = firebase.database().ref('webapp').push().set(
            //     {
            //         kid: input.value
            //     }
            // );
            // firebasePush(inputZip);
            //push itself
            // var mailsRef = firebase.database().ref('webapp').push().set(
            //     {
            //         zip: input.value
            //     }
            // );

            //shows alert if everything went well.
            return alert('Data has been registered in the database');
        })
    }