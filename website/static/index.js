function deleteTodo(id) {
	fetch("/delete-todo", {
		method: "POST",
		body: JSON.stringify({ id: id }),
	}).then((_res) => {
		window.location.href = "/"
	})
}
