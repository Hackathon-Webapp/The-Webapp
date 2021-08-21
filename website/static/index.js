// function deleteTodo(id) {}

const deleteTodo = (id) => {
	fetch("/delete-todo", {
		method: "POST",
		body: JSON.stringify({ id: id }),
	}).then((_res) => {
		window.location.href = "/todo"
	})
}
