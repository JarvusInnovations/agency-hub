import { createApp } from 'vue'
import unrest from '@unrest/vue'
import form from '@unrest/vue-form'
import auth from '@unrest/vue-auth'

import App from '@/App.vue'
import router from '@/router'
import store from '@/store'

import '@unrest/tailwind/dist.css'
import '@/styles/index.css'

auth.configure({
  oauth_providers: [],
  enabled: !process.env.VUE_APP_OFFLINE,
  signup_enabled: false,
  getDisplayName: (user) => user.email.split("@")[0],
})


createApp(App)
  .use(router)
  .use(store)
  .use(form.plugin)
  .use(auth.plugin)
  .use(unrest.plugin)
  .use(unrest.ui)
  .mount('#app')
