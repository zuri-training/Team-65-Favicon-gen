const container = document.querySelectorAll('.faq_container');

container.forEach(item => {
   item.addEventListener('click', () => {
      item.classList.toggle('active')
      container.forEach(card => {
         if (card != item) {
            card.classList.remove('active')
         }
      })
   })
})