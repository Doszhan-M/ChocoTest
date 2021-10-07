// Удалить ToDo
function toDoDelete(id) {
    tokenStorage = window.localStorage.getItem('token')

    let body = JSON.stringify({
        data: `${id}`
    });

    const options = {
        method: 'DELETE',
        body : body,
        headers: {
            "Content-type": "application/json",
            "Authorization": `Token ${tokenStorage}`
        }
    }
    // вывести все блоки
    fetch(`/api/todoupdel/`, options)
        .then(response => response.json())
        .then(json => { 
            alert(json.detail)
            todo__wrapper.innerHTML = ``

            showTaskListPage()
        })
        .catch(json => { 
            alert('ToDo удален') 
            todo__wrapper.innerHTML = ``
            showTaskListPage()
        })

}


// Изменить ToDo
async function toDoUpdate(id, headline, desc, optionsIndex, deadline) {
    tokenStorage = window.localStorage.getItem('token')

    let body = JSON.stringify({
        data: `${id}`,
        headline: headline,
        description: desc,
        priority: optionsIndex,
        deadline: deadline
    });
    const options = {
        method: 'PATCH',
        body : body,
        headers: {
            "Content-type": "application/json",
            "Authorization": `Token ${tokenStorage}`
        }
    }

    // изменить
    let response =await fetch(`/api/todoupdel/`, options).then((response) => {
        if (response.ok) {
            alert('ToDo изменен')
            todo__wrapper.innerHTML = ``
            showTaskListPage()
        } 
        if (response.status == 403) {
            alert('У вас недостаточно прав для выполнения данного действия.')
        }
    })


}