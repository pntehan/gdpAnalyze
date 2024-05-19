<template>
  <router-view></router-view>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    const debounce = (callback, delay) => {
      let tid = 0
      return function (args) {
        const ctx = self;
        tid && clearTimeout(tid);
        tid = setTimeout(() => {
          callback.apply(ctx, args);
        }, delay);
      };
    };

    const _ = (window).ResizeObserver;
    (window).ResizeObserver = class ResizeObserver extends _ {
      constructor(callback) {
        callback = debounce(callback, 20)
        super(callback);
      }
    }
  },
});
</script>

<style lang="less">
#app {
  height: 100%;
  width: 100%;
}
</style>
