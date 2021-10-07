let tokenStorage = window.localStorage.getItem('token')
let main = document.querySelector('main')
sign__block = document.querySelector('.sign__block')


// Функция показа страницы авторизации
function showLoginPage() {
    tokenStorage = window.localStorage.getItem('token')

    document.querySelector('.todoadd__wrapper').innerHTML = ``
    document.querySelector('.todo__wrapper').innerHTML = ``
    if (tokenStorage == 'undefined') {
        tokenStorage = window.localStorage.removeItem('token')
    }
    console.log('tokenStorage', tokenStorage)
    if (tokenStorage == null) {
        let LoginForm = `
        <div class="sign">
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
        </div>
        `
        sign__block.innerHTML = LoginForm

        let form_button = document.querySelector('#form_button')
        let form_btn_signup = document.querySelector('#form_btn_signup')

        form_button.addEventListener('click', () => {
            signIn()
        })

        form_btn_signup.addEventListener('click', () => {
            showSignUpPage()
        })

    } else {
        sign__block.innerHTML = ``
        showTaskListPage()
    }

}

// Функция авторизации пользователя
async function signIn() {
    let form_email = document.querySelector('#form_email')
    let form_pass = document.querySelector('#form_pass')
    let email = form_email.value
    let pass = form_pass.value

    let body = JSON.stringify({
        "user": {
            email: `${email}`,
            password: `${pass}`
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
    showLoginPage()
}


// Функция показа страницы регистрации
function showSignUpPage() {
    tokenStorage = window.localStorage.getItem('token')
    console.log('tokenStorage', tokenStorage)
    if (tokenStorage == 'undefined') {
        tokenStorage = window.localStorage.removeItem('token')
    }
    console.log('tokenStorage', tokenStorage)
    if (tokenStorage == null) {
        let SignUpForm = `
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
                <input type="radio" id="simple" name="usertype" value="Simple">
                <label for="simple">Simple User</label>
            </div>

            <div class="signin__text">
                <input type="radio" id="Employee" name="usertype" value="Employee">
                <label for="Employee">Employee User</label>
            </div>

            <div class="signin__text">
                <input type="radio" id="Administrator" name="usertype" value="Administrator">
                <label for="Administrator">Administrator User</label>
            </div>

            <div class="container-login100-form-btn">
                <button id="form_button" type="button" class="login100-form-btn">
                    Register
                </button>
            </div>
        </form>
        `
        sign__block.innerHTML = SignUpForm

        let form_button = document.querySelector('#form_button')
        form_button.addEventListener('click', () => {
            signUn()
        })
    } else {
        sign__block.innerHTML = ``
        showTaskListPage()
    }
}

// Функция регистрации пользователя
async function signUn() {
    let form_email = document.querySelector('#form_email')
    let form_pass = document.querySelector('#form_pass')
    let form_username = document.querySelector('#form_username')

    let usertype = document.querySelector('input[name="usertype"]:checked').value;
    if (usertype == 'Administrator') {
        is_employee = false
        is_administrator = true
    } else if (usertype == 'Employee') {
        is_employee = true
        is_administrator = false
    } else {
        is_administrator = false
        is_employee = false
    }
    
    let body = JSON.stringify(
        {
        'user': {
            username : form_username.value,
            email : form_email.value,
            password : form_pass.value,
            is_employee : is_employee,
            is_administrator : is_administrator
            }
        }
    );
    const options = {
        method: 'POST',
        body: body,
        headers: {
            "Content-type": "application/json",
        }
    }
    // Отправить post запрос серверу
    await fetch(`/api/users/signup/`, options)
        .then(response => response.json())
        .then(json => {
            if (json.token != 'undefined') {
                // записать токен в storage
                window.localStorage.setItem('token', json.token);
                tokenStorage = window.localStorage.getItem('token')
                console.log('tokenStorage', tokenStorage)
            }   else {
                alert('Неправильно заполнены поля')
                showSignUpPage
            }
        })

    showLoginPage()

}

