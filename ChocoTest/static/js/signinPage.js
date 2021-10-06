

let main = document.querySelector('main')
// let administrator = document.querySelector('#Administrator')


// Функция проверки токена в storage
function tokenCheck() {
    let tokenStorage = window.localStorage.getItem('token')
    console.log('tokenStorage', tokenStorage)
    if (tokenStorage == null) {
        let = signinForm = `
        <form class="login100-form validate-form">
            <span class="login100-form-title">
                Member Login
            </span>

            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                <input id="form_email" class="input100" type="text" name="email" placeholder="Email">
                <span class="focus-input100"></span>
                <span class="symbol-input100">
                    <i class="fa fa-envelope" aria-hidden="true"></i>
                </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
                <input id="form_pass" class="input100" type="password" name="pass" placeholder="Password">
                <span class="focus-input100"></span>
                <span class="symbol-input100">
                    <i class="fa fa-lock" aria-hidden="true"></i>
                </span>
            </div>
            
            <div class="container-login100-form-btn">
                <button id="form_button" type="button" class="login100-form-btn">
                    Login
                </button>
            </div>

            <div class="signin__text">
                <button id="form_btn_signup" type="button" class="form_btn_signup">
                    Create your Account
                </button>
            </div>
        </form>
        `
        main.innerHTML = signinForm
    } else {
        main.innerHTML = `есть токен`
    }
}


function showSigninPage() {
    tokenCheck()
    let form_button = document.querySelector('#form_button')
    let form_btn_signup = document.querySelector('#form_btn_signup')

    form_button.addEventListener('click', () => {
        signIn()
        // showSigninPage()
    })

    form_btn_signup.addEventListener('click', () => {
        showSignUpPage()
    })
}


// Страница авторизации
function showSignUpPage () {

    if (tokenStorage == null) {
        let = signinForm = `
        <form class="login100-form validate-form">
        <span class="login100-form-title">
            Register
        </span>

        <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
            <input id="form_username" class="input100" type="text" name="email" placeholder="Username">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
            </span>
        </div>

        <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
            <input id="form_email" class="input100" type="text" name="email" placeholder="Email">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
            </span>
        </div>

        <div class="wrap-input100 validate-input" data-validate = "Password is required">
            <input id="form_pass" class="input100" type="password" name="pass" placeholder="Password">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
            </span>
        </div>

        <div class="signin__text">
            <input type="radio" id="simple" name="usertype">
            <label for="simple">Simple User</label>
        </div>

        <div class="signin__text">
            <input type="radio" id="Employee" name="usertype">
            <label for="Employee">Employee User</label>
        </div>

        <div class="signin__text">
            <input type="radio" id="Administrator" name="usertype">
            <label for="Administrator">Administrator User</label>
        </div>

        <div class="container-login100-form-btn">
            <button id="form_button" type="button" class="login100-form-btn">
                Register
            </button>
        </div>
    </form>
        `
        main.innerHTML = signinForm
    } else {
        main.innerHTML = `есть токен`
    }


}

// Функция авторизации пользователя
async function signIn() {
    let form_email = document.querySelector('#form_email')
    let form_pass = document.querySelector('#form_pass')

    let body = JSON.stringify({
        'user': {
            email: form_email.value,
            password: form_pass.value
        }
    });
    const options = {
        method: 'POST',
        body: body,
        headers: {
            "Content-type": "application/json",
        }
    }
    // Отправить post запрос серверу
    await fetch(`/api/users/signin/`, options)
        .then(response => response.json())
        .then(json => {
            // записать токен в storage
            window.localStorage.setItem('token', json.token);
        })
    console.log('token', window.localStorage.getItem('token'))
    tokenCheck()
    
}



// Функция регистрации пользователя
function signUn() {
    let body = JSON.stringify({
        'user': {
            email: form_email.value,
            password: form_pass.value
        }
    });
    const options = {
        method: 'POST',
        body: body,
        headers: {
            "Content-type": "application/json",
        }
    }
    // Отправить post запрос серверу
    fetch(`/api/users/signin/`, options)
        .then(response => response.json())
        .then(json => {
            // записать токен в storage
            window.localStorage.setItem('token', json.token);
        })
}




// let usertype = document.querySelector('input[name="usertype"]:checked').value;
// console.log(usertype)