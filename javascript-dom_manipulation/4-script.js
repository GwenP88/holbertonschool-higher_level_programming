const ul = document.querySelector('.my_list');
const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  ul.appendChild(newLi);
});
