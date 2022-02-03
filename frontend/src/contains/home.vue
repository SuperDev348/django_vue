<template>   
    <v-container
        class="pa-10"
    >
        <validation-observer
            ref="observer"
        >
            <validation-provider
                v-slot="{ errors }"
                rules="required|max:50"
                name="title"
            >
                <v-text-field
                    v-model="title"
                    :counter="50"
                    :error-messages="errors"
                    label="Title"
                    required
                ></v-text-field>
            </validation-provider>
            <validation-provider
                v-slot="{ errors }"
                rules="required|max:500"
                name="remark"
            >
                <v-textarea
                v-model="remark"
                :counter="500"
                :error-messages="errors"
                label="Remark"
                required
                ></v-textarea>
            </validation-provider>

            <v-btn
                class="mr-4"
                @click="add"
                color="success"
            >
                Add
            </v-btn>
        </validation-observer>
        <v-simple-table>
            <template v-slot:default>
                <thead>
                    <tr>
                        <th class="text-left">
                            Title
                        </th>
                        <th class="text-left">
                            Remark
                        </th>
                        <th class="text-left">
                            Detail
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                    v-for="item in items"
                    :key="item.id"
                    >
                        <td>{{ item.title }}</td>
                        <td>{{ item.remark }}</td>
                        <td>
                            <router-link :to="'/todo/'+item.id" style="text-decoration: none;">
                                <v-btn
                                    class="mr-4"
                                    color="success"
                                >
                                    Detail
                                </v-btn>
                            </router-link>
                        </td>
                    </tr>
                </tbody>
            </template>
          </v-simple-table>
    </v-container>
</template>
<script>
    
    import { required, max } from 'vee-validate/dist/rules'
    import { extend, ValidationObserver, ValidationProvider } from 'vee-validate'
    import axios from 'axios'

    extend('required', {
        ...required,
        message: '{_field_} can not be empty',
    })
    extend('max', {
        ...max,
        message: '{_field_} may not be greater than {length} characters',
    })

    export default {
        name: 'Home',
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        computed : {
            
        },
        methods: {
            add : function(){
                let data = {'title':this.title, 'remark':this.remark};
                axios.post(this.base_url+'/items', data)
                .then((response)=>{
                    console.log(response);
                    this.refresh();
                })
            },
            refresh : function(){
                axios.get(this.base_url+'/items')
                .then((response)=>{
                    this.items = response.data;
                    console.log(response);
                })
            }
        },
        mounted: function() {
            this.refresh();
        },
        data: () => ({
            base_url:'http://127.0.0.1:8000/api',
            title:'',
            remark:'',
            items:[]
        })
    };
</script>