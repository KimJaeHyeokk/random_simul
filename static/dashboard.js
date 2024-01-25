document.addEventListener('DOMContentLoaded', function() {

    DashboardAjax();
    setInterval(DashboardAjax, 1000)

    btn();
});

// Ajax통신
function DashboardAjax(btn){
    let formData = new FormData(); // 새로운 폼 객체 생성
    formData.append('btn', btn); 
    let xhr = new XMLHttpRequest();
    
    const csrftoken = getCookie('csrftoken')
    xhr.onload = function() {
        if (xhr.readyState === xhr.DONE && xhr.status === 200){
            const result_json = xhr.response;
            const result = JSON.parse(result_json);
       
            document.getElementById("a").innerHTML = result['a']
        }
        else if (xhr.status !== 200) {
            console.log('failed')
        }
    };
    xhr.open("POST", "/main/", true);
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.send(formData);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function btn() {
    const button = document.querySelector('.btn button');

    button.addEventListener('click', function () {
        if (button.classList.contains('on')) {
            button.classList.remove('on');
            button.classList.add('off');
            DashboardAjax("on")
        } else {
            button.classList.remove('off');
            button.classList.add('on');
            DashboardAjax("off")
        }
    });
}