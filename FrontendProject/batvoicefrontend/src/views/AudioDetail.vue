<template>
    <h1>Hello</h1>
    <div>
        <p>Title</p>
        <p>Description {{ obj.description }}</p>
        <p>Customer {{ obj.customer }}</p>
    </div>

</template>
<script>
import axios from 'axios'
export default {
    name: 'audiodetail',
    date() {
        return {
            obj: {}
        }
    },
    mounted() {
        this.getAudio()
    },
    methods: {
        getAudio() {
            const id = this.$route.params.id
            axios.get(`/api/${id}/`)
                .then(response => this.obj = response.data )
                .catch( error => console.log(error))
        },
    },
}
</script>
