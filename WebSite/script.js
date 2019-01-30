var config = {
    apiKey: "AIzaSyDsPtVdNNbBZGXwTW2x61z7Y4ZrUn9PWMY",
    authDomain: "special-numbers.firebaseapp.com",
    databaseURL: "https://special-numbers.firebaseio.com/",
};
// storageBucket: "bucket.appspot.com"
firebase.initializeApp(config);

let database = firebase.database();
let activeCompany = 'E' // one of E, V, W, O

function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
    
}


function writeUserData(userId, name, email, imageUrl) {
    firebase.database().ref('users/' + userId).set({
      username: name,
      email: email,
      profile_picture : imageUrl
    });
  }


function getPhoneNumbers(company, type){
    ref = database.ref(`/${company}-${type}`)
    ref.once('value', function(phonesSH) { 
        phonesSH.forEach(phoneSH => {
            phone = phoneSH.key
            status = phoneSH.val()
            console.log(phone);            
            console.log(status);
            if(status !== 'Available') return
            alert(phone.key)
        });
    });
}

function vipOnly(){
    writeUserData(123, 'ammar', 'ammaralsayed55@gmail.com', 'https://avatars1.githubusercontent.com/u/23727296?s=460&v=4')
    writeUserData('5wab', 'omar samir', 'omarsamir@gmail.com', 'https://avatars1.githubusercontent.com/u/23727296?s=460&v=4')
}

function specialOnly(){

    getPhoneNumbers('Etisalat', 'vip')
}

function setActiveCompany(who){
    activeCompany = who
    
}

function vipAndSpecial(){
}









var appConfig = {
    companyColors: {
        'O': '#006699',
        'E': '#446699',
        'W': '#123456',
        'V': '#789456',
    },
}