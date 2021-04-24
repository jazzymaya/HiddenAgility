const toggleModal = () => {
    document.querySelector('.modal')
    .classList.toggle('modal___Hidden');
    
    console.log('Button has been pressed');
};

document.querySelector('#Show-modal').addEventListener('click', toggleModal);

document.querySelector('.modal___Closebar span').addEventListener('click', toggleModal);