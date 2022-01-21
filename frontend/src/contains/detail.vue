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
            getItem : function(){
                if(this.id != -1){
                    axios.get(this.base_url+'/items/'+this.id)
                    .then((response)=>{
                        this.title = response.data.title;
                        this.remark = response.data.remark;
                        console.log(response);
                    })
                }
            },
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