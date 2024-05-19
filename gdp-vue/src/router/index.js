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
        path: "/exam",
        name: "exam",
        component: () => import('@/views/user/Exam.vue')
      },
      {
        path: "/announcement",
        name: "announcement",
        component: () => import('@/views/user/Announcement.vue')
      },
      {
        path: "/new",
        name: "new",
        component: () => import('@/views/user/New.vue')
      },
      {
        path: "/new/:id",
        name: "newDetail",
        component: () => import("@/views/user/NewDetail.vue")
      },
      {
        path: "/book",
        name: "book",
        component: () => import("@/views/user/Book.vue")
      },
      {
        path: "/consult",
        name: "consult",
        component: () => import("@/views/user/Consult.vue")
      },
      {
        path: "/user",
        name: "user",
        component: () => import("@/views/user/User.vue")
      },
      {
        path: "/star",
        name: "star",
        component: () => import("@/views/user/Star.vue")
      },
      {
        path: "/msg",
        name: "msg",
        component: () => import("@/views/user/Msg.vue")
      }
    ]
  },
  // 管理员部分
  {
    path: '/admin',
    component: () => import("@/components/AdminLayout.vue"),
    name: 'admin',
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: () => import("@/views/admin/Dashboard.vue"),
        meta: { menuIndex: '/admin' }
      },
      {
        path: 'userData',
        name: 'UserData',
        component: () => import("@/views/admin/UserData.vue"),
        meta: { menuIndex: '/admin/userData' }
      },
      {
        path: 'consultData',
        name: 'ConsultData',
        component: () => import("@/views/admin/ConsultData.vue"),
        meta: { menuIndex: '/admin/consultData' }
      },
      {
        path: 'systemData',
        name: 'SystemData',
        component: () => import("@/views/admin/SystemData.vue"),
        meta: { menuIndex: '/admin/systemData' }
      },
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
    component: () => import("@/views/user/Login.vue")
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/user/Register.vue")
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
