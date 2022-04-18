function showFoam(evt) {
  $.get('/images_foaming', (res) => {
        
    let foa = res.foam;
    let user = res.user;
    let container_div = "<div class='container'>"; 
      
    $('#images_foaming').empty().append(container_div);
    for (let i=0; i < foa.length; i++) {
        current_foa = foa[i]
        let out = `<p>${current_foa['image_id']}</p>` 
         + `<img src=${current_foa['url']} width="330" height="280"><br>`
         + `lastModified: ${current_foa['lastModified']}<br>`
         ;
  
       $('#images_foaming').append(out);
      }  
      $('#images_foaming').append("</div>");
  
    });
    $('#images').hide();
    console.log(out)
  }   

  $(document).ready(showFoam)

  function showNotFoam(evt) {
    $.get('/images_not_foaming', (res) => {
          
      let foa_not = res.not_foam;
      let user = res.user;
      let container_div = "<div class='container'>"; 
        
      $('#images_not_foaming').empty().append(container_div);
      for (let i=0; i < foa_not.length; i++) {
          current_foa_not = foa_not[i]
          let out = `<p>${current_foa_not['image_id']}</p>` 
           + `<img src=${current_foa_not['url']} width="330" height="280"><br>`
           + `lastModified: ${current_foa_not['lastModified']}<br>`
           ;
    
         $('#images_not_foaming').append(out);
        }  
        $('#images_not_foaming').append("</div>");
    
      });
      $('#images').hide();
      console.log(out)
    }   
  
    $(document).ready(showNotFoam) 