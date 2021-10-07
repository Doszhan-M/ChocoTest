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
        await fetch(`/api/todolist/`, options)
            .then(response => response.json())
            .then(json => { 
                // пройтись по каждому блоку 
                for (let elem in json) {
                    console.log(json[elem]);
                    let todoCard = document.createElement('div');
                    todoCard.innerHTML = `
                    <form action="">
                    <div class="todo">
                        <input class="todo__headline" type="text" value="${json[elem].headline}">
                        <textarea class="todo__desc">${json[elem].description}</textarea>
                        <div class="todo__priority">
                            <p>Приоритет</p>
                            <select>
                                <option>низкий</option>
                                <option>нормальный</option>
                                <option>высокий</option>
                            </select>
                        </div>
                        <div class="todo__deadline">
                            <label for="deadline">Deadline:</label>
                            <input id="deadline" class="todo__time" type="datetime-local" value="2018-06-12T19:30">
                        </div>
                        <div class="todo__btns">
                            <button class="btn todo__change">Изменить</button>
                            <button class="btn todo__del">Удалить</button>
                        </div>
                    </div>
                </form>
                    `
                    todo__wrapper.append(todoCard)
                    todo__headline = document.querySelector('.todo__headline')
                    todo__desc = document.querySelector('.todo__desc')

                    let option = document.querySelectorAll('option')
                    option[json[elem].priority].selected="selected"

                }



                // todo__headline.value = json[0].headline
                // todo__desc.value = json.description
            })


    }
}

// Функция запроса списка todo
async function getTodoList() {

}