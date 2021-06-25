new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
    news: []
    },
    mounted: function () {
        this.getNews();
        console.log(this.news)
    },
    methods: {
        getNews: function () {
            fetch('/api/v1/news/')
                .then(function (response) {
                    return response.json();
                })
                .then((json) => {
                    this.news = json;
                })
        },
        votar: function (id) {
            fetch('/api/v1/news/', {
                headers: {
                    'Content-type': 'application/json'
                },
                method: 'PUT',
                body: JSON.stringify(
                    {
                        'id': id,
                    }
                )
            })
            .then((json) => {
                // Usamos la información recibida como necesitemos
                this.getNews()
            });
        }
    }
})