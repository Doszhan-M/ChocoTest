todo__wrapper = document.querySelector('.todo__wrapper')

async function showTaskListPage() {
    tokenStorage = window.localStorage.getItem('token')
    if (tokenStorage == null) {
        showLoginPage()
    } else {

        const options = {
            method: 'GET',
            headers: {
                "Content-type": "application/json",
                "Authorization": `Token ${tokenStorage}`
            }
        }
        // вывести все блоки
        await fetch(`/api/todolist/`, options)
            .then(response => response.json())
            .then(json => {
                // пройтись по каждому блоку 
                for (let elem in json) {
                    let todoCard = document.createElement('div');
                    date = json[elem].deadline
                    if (date != null) {
                        date = date.slice(0, 16)
                    } 
                    todoCard.innerHTML = `
                    <form action="">
                    <div class="todo">
                        <input class="todo__headline" id="input${json[elem].id}" type="text" value="${json[elem].headline}">
                        <textarea class="todo__desc" id="desc${json[elem].id}">${json[elem].description}</textarea>
                        <div class="todo__priority">
                            <p>Приоритет</p>
                            <select id="select${json[elem].id}">
                                <option>низкий</option>
                                <option>нормальный</option>
                                <option>высокий</option>
                                <option>Не присвоен</option>
                            </select>
                        </div>
                        <div class="todo__deadline">
                            <label for="deadline${json[elem].id}">Deadline:</label>
                            <input id="deadline${json[elem].id}" class="todo__time" type="datetime-local" value="${date}">
                        </div>
                        <div class="todo__btns">
                            <button id="change${json[elem].id}" type="button" class="btn todo__change">Изменить</button>
                            <button id="delete${json[elem].id}" type="button" class="btn todo__del">Удалить</button>
                        </div>
                    </div>
                    </form>
                    `
                    todo__wrapper.append(todoCard)
                    todo__headline = document.querySelector('.todo__headline')
                    todo__desc = document.querySelector('.todo__desc')

                    // Выставить правильный приоритет
                    let myOptions = document.querySelector(`#select${json[elem].id}`)
                    let options = document.querySelectorAll('option')
                    let optionValue = options[json[elem].priority].value
                    for (var i, j = 0; i = myOptions.options[j]; j++) {
                        if (i.value == optionValue) {
                            myOptions.selectedIndex = j;

                            break;
                        }
                    }
                    //Обработчик удаления таска
                    todo__del = document.querySelector(`#delete${json[elem].id}`)
                    todo__del.addEventListener('click', () => {
                        let id = json[elem].id
                        toDoDelete(id)
                    })

                    //Обработчик изменения таска
                    todo__change = document.querySelector(`#change${json[elem].id}`)
                    todo__change.addEventListener('click', () => {
                        let id = json[elem].id
                        let headline = document.querySelector(`#input${json[elem].id}`).value
                        let desc = document.querySelector(`#desc${json[elem].id}`).value
                        let optionsIndex = myOptions.selectedIndex
                        let deadline = document.querySelector(`#deadline${json[elem].id}`).value
                        toDoUpdate(id, headline, desc, optionsIndex, deadline)
                    })
                }
            })


        // отобразить кнопку выхода
        let logoutBlock = document.querySelector('.user_info')
        logoutBlock.innerHTML = `<button id="user_info" class="btn todo__del">Выйти</button>`
        let logout = document.querySelector('#user_info')
        logout.addEventListener('click', () => {
            window.localStorage.removeItem('token');
            document.querySelector('.add_task').innerHTML = ``
            document.querySelector('.todoadd__wrapper').innerHTML = ``
            logoutBlock.innerHTML = ``
            todo__wrapper.innerHTML = ``
            showLoginPage()
        })

        // отобразить кнопку добавления таска
        let addBlock = document.querySelector('.add_task')
        addBlock.innerHTML = `<button id="addtodo" class="btn todo__change">Добавить ToDo</button>`
        let addToDo = document.querySelector('#addtodo')

        addToDo.addEventListener('click', () => {
            const options = {
                method: 'POST',
                headers: {
                    "Content-type": "application/json",
                    "Authorization": `Token ${tokenStorage}`
                }
            }
            // вывести все блоки
            fetch(`/api/todocreate/`, options).then((response) => {
                if (response.status == 403) {
                    alert('У вас недостаточно прав для выполнения данного действия')
                }
                if (response.status == 201) {
                    showAddTaskPage()
                }
                if (response.status == 400) {
                    showAddTaskPage()
                }
                return response
            }).then(response => response.json())
                .then(json => {console.log(json)})
                .catch(json => {
                    showLoginPage()
                })
        })

    }
}