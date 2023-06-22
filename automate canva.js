// function waitForElement(searchFN, timeout = 5000) {
//     // Promise has an input of an executor function, that has an input of two other functions
//     // so the input function(resolve, reject) { }, the {} defines the function inside the brackets
//     // mi initial error here was forgetting the (), el = searchFN redefines el as the function
//     // this of course both exists, and will return undefined/ definitely does not have a .click() function
//     // need to remember to have el be what the function returns when called, ie el = func()
//     return new Promise(function(resolve, reject) {
//         let el = searchFN()
//         if (el) {
//             resolve(el);
//             return;
//         }
//         // setInterval takes a function that it performs, and an interval that tells it how often to perform it
//         let intervalId = setInterval(function() {
//             el = searchFn();
//             if (el) {
//                 // this turns off the setInterval function, if you don't have it, it will just keep running forever
//                 clearInterval(intervalId);
//                 resolve(el);
//             }
//         }, 300);
//         setTimeout(function() {
//             clearInterval(intervalId);
//             reject(new Error('Element not found after ${timeout / 1000} seconds'))
//         }, timeout)
//     })
// }

// helper function that can be reused for different searches
// returns the first item of the type with that text content
// keep in mind, this will only find it if the textContent exactly matches, ie download will not work if the textContent is Download or download now
// it could be modified to includes() or to have it be lowerCase (type.textContent) === lowerCase(keyWord)
// Also keep in mind that both inputs must be strings
function searchByTagName(type, keyWord){
    let typeList = Array.from(document.getElementsByTagName(type));
    return typeList.find(type => type.textContent === keyWord)
    

}

let button1 = document.querySelector('button[aria-controls="header_item4"]')

let findButton2 = function() {
    return searchByTagName('button', 'Download')
}



let findButton3 = function() {
    return document.querySelector('button[type="submit"]')
}

button1.click()

function delay(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
  }
  
async function pause(milliseconds, searchFN) {
    
    await delay(milliseconds); // Pause for 2 seconds
    
    // Place your code here that needs to run after the pause
    let button = searchFN()
    if (button) {
      button.click();
    }
  }
  
  pauseExample(2000, findButton2)





//waitForElement(findbutton2).then(function(button){ button.click()})

// let findButton1 = function() {
//     return document.querySelector('button[aria-controls="header_item4"]')

// }



// let findButton2Alt = function () {
//     let buttons = Array.from(document.getElementsByTagName("button"));
//     return buttons.find(button => button.textContent === 'Download');
// };

// let findButton3 = function (){
//     button = document.querySelector('button[aria-label="File type"]')
//     return button
// }

// waitForElement(findButton1)
//     .then(function(button) {
//         if(button === null) {
//             console.log('Button not found.');
//         } else if(typeof button.click === 'function') {
//             button.click();
//         } else {
//             console.log('Returned object is not a button:', button);
//         }
//     })
//     .catch(function(error){console.error(error)})

// waitForElement(findButton2Alt)
//     .then(function(button) {button.click();})
//     .catch(function(error) {
//         console.error(error)
//     })

// waitForElement(findButton3)
//     .then(function(button) {button.click();})


