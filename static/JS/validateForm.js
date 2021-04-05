// Once typing stops, check if empty and enable / disable button
/*
function stoppedTyping(textBoxId, buttonId) {
    let theButton = document.getElementById(buttonId)
    let theText = document.getElementById(textBoxId)
    
    if (theText.value.length > 0) { 
        //document.getElementById(buttonName).disabled = false; 
        theButton.disabled = false
    } else { 
        //document.getElementById(buttonName).disabled = true;
        theButton.disabled = true
    }
}
*/

// Verify that signup form is valid by checking that no fields are empty
function validateSignup(formId) {
    let elems = document.getElementById(formId).elements;   // Get a list of elements from the form
    let alertMsg = 'Please fill in '                        // Alert message phrasing
    for(let i = 0; i < elems.length; i++) {                 // Loop through all form fileds
        if (elems[i].name === 'Email') {                    // If email field
            continue                                        // Continue, this is optional
        }
        if (elems[i].value === '') {                        // If a field is blank
            alertMsg += elems[i].name                       // Add the field name to the alert message
            alert(alertMsg);                                // Push the alert
            return false                                    // Fail to form submission
        }
    }

}