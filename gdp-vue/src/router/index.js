import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  // 用户部分
  {
    path: '/',
    name: 'user',
    component: () => import('@/views/user/index.vue'),
    children: [
      {
        path: "/home",
        name: "home",
        component: () => import('@/views/user/Home.vue')
      },
      {
        path: "/dataAnalyse",
        name: "dataAnalyse",
        component: () => import('@/views/user/DataAnalyse.vue')
      },
      {
        path: "/dataShow",
        name: "dataShow",
        component: () => import('@/views/user/DataShow.vue')
      },
      {
        path: "/dataPredict",
        name: "dataPredict",
        component: () => import("@/views/user/DataPredict.vue")
      },
      {
        path: "/user",
        name: "user",
        component: () => import("@/views/user/User.vue")
      }
    ]
  },
  // 公共部分
  {
    path: "/404",
    name: "404",
    component: () => import("@/views/BanView.vue")
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/Login.vue")
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/Register.vue")
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  // base:
  //   process.env.NODE_ENV !== "production"
  //     ? process.env.BASE_URL
  //     : process.env.BASE_URL  ,
  routes,
  scrollBehavior(to, from, savedPosition) {
    // return { x: 0, y: 0 };
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  }
});

export default router;

// 全局路由守卫
router.beforeEach((to, from, next) => {
  if (to.fullPath.includes("404")) {
    next()
  }
  if (to.matched.length == 0) {
    next("/404")
  }
  if (to.fullPath.includes("login") | to.fullPath.includes("register")) {
    next()
  } 
  else if (localStorage.getItem("user_info")) {
    let user_info = JSON.parse(localStorage.getItem("user_info"))
    // 管理员检查
    if (to.fullPath.includes("admin")) {
      if (user_info.role == "管理员") {
        next()
      }
      else {
        next("/404")
      }
    }
    else {
      next()
    }
  }
  else {
    next("/login")
  }
})
