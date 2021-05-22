
function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');


        async function makeRequest(url, method='POST', body) {
            let headers ={
                'X-CSRFToken':csrftoken
            }
        let response = await fetch(url, {method, headers:headers, body:body});
            if (response.ok) {  // нормальный ответ
                let resp = await response.json();
            return resp
            }
            else {            // ошибка
            let error = new Error(response.statusText);
            error.response = response;
            throw error;
            }
        }

        CalculateAction = async (event) => {
            event.preventDefault()
            let input = event.target
            let url = input.dataset.url
            let a = document.getElementById('FirstNumber').value
            let b = document.getElementById('SecondNumber').value
            try {
                let result = await makeRequest(url, "POST", JSON.stringify({'A': a, "B": b}))
                console.log(result['answer'])
                if(document.getElementById('print_result')){
                document.getElementById('print_result').innerHTML = ""
                }
                let info_p = document.createElement('p')
                info_p.innerText = `Результат : ${result['answer']}`
                info_p.setAttribute('class', 'mt-3')
                info_p.style.color = 'green'
                let div_result = document.getElementById("print_result")
                div_result.appendChild(info_p)
            }
            catch (error){
                let e = await error.response.json()
                console.log(e.error)
                if(document.getElementById('print_result')){
                document.getElementById('print_result').innerHTML = ""
                }
                let info_p = document.createElement('p')
                info_p.innerText = `Ошибка :${e.error}`
                info_p.setAttribute('class', 'mt-3')
                info_p.style.color = 'red'
                let div_result = document.getElementById("print_result")
                div_result.appendChild(info_p)
            }
        }