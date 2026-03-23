document.addEventListener('DOMContentLoaded', function () {
  const ul = document.querySelector('.my_list');
  const add = document.querySelector('#add_item');
  const remove = document.querySelector('#remove_item');
  const clear = document.querySelector('#clear_list');

  add.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });

  remove.addEventListener('click', function () {
    const lastChild = ul.lastElementChild;
    if (lastChild) {
      ul.removeChild(lastChild);
    }
  });

  clear.addEventListener('click', function () {
    ul.innerHTML = '';
  });
});
