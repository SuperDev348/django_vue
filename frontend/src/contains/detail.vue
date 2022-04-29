<template>
    <div style="padding: 50px 100px;">
        <div>
            id: {{this.id}}
        </div>
        <div>
            title: {{this.title}}
        </div>
        <div>
            remark: {{this.remark}}
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    
    export default {
        name: 'Detail',
        components: {
        },
        methods : {
        },
        computed : {
            
        },
        mounted: function() {
            this.id = this.$route.params.id;    
            this.getItem();
        },
        data () {
            return {
                base_url:'http://127.0.0.1:8000/api',
                title:'',
                remark:'',
                id:-1,
            }
        },
    }
</script>
<style>
</style>