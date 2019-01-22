import Vue from 'vue';
import VueKonva from 'vue-konva';
import './plugins/vuetify';
import App from './App.vue';

Vue.config.productionTip = false;

Vue.use(VueKonva);

new Vue({
  render: h => h(App)
}).$mount('#app');
