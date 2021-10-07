async function showAddTaskPage() {
    tokenStorage = window.localStorage.getItem('token')
    if (tokenStorage == null) {
        showLoginPage()
    } else {
        todo__wrapper.innerHTML = ``
        let todoCard = document.createElement('div');
        todoCard.innerHTML = `
        <form action="">
        <div class="todo">
            <input class="todo__headline" type="text" value="egseef">
            <textarea class="todo__desc">44444</textarea>
            <div class="todo__priority">
                <p>Приоритет</p>
                <select id="select">
                    <option>низкий</option>
                    <option>нормальный</option>
                    <option>высокий</option>
                    <option selected>Не присвоен</option>
                </select>
            </div>
            <div class="todo__deadline">
                <label for="deadline">Deadline:</label>
                <input id="deadline" class="todo__time" type="datetime-local">
            </div>
            <div class="todo__btns">
                <button type="button" id="addtask" class="btn todo__change">Добавить</button>
            </div>
        </div>
        </form>
        `
        let todoadd__wrapper = document.querySelector('.todoadd__wrapper')
        todoadd__wrapper.append(todoCard)

        let addBtn = document.querySelector('#addtask')
        console.log(addBtn)
        addBtn.addEventListener('click', () => {
            todo__headline = document.querySelector('.todo__headline')
            todo__desc = document.querySelector('.todo__desc')
            todo__select = document.querySelector('#select')
            deadline = document.querySelector('#deadline')
            console.log(deadline.value)
            let body = JSON.stringify({
                    headline: todo__headline.value,
                    description: todo__desc.value,
                    priority: todo__select.selectedIndex,
                    deadline: deadline.value
            });
            const options = {
                method: 'POST',
                body: body,
                headers: {
                    "Content-type": "application/json",
                    "Authorization": `Token ${tokenStorage}`
                }
            }
            fetch(`/api/todocreate/`, options)
                .then(response => response.json())
                .then(json => {
                    alert((json.errors.error))
                })
                .catch(json => {
                    alert('ToDo добавлен')
                    location.reload() 
                })
        })
    }
}


