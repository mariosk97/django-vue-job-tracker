<template>
  <Toast />
  <RouterView />
</template>

<script>
    import Toast from '@/components/Toast.vue'
    import { useUserStore } from '@/stores/user'
    import axios from 'axios'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
    },

        components: {
            Toast
        },

        beforeCreate() {
            this.userStore.initStore()
            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token
            }
            else {
                axios.defaults.headers.common["Authorization"] = ""
            }
        }
    }
</script>


