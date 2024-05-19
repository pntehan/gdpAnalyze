import { get } from "../utils/request"

export const initDashboard = () => {
  return get("/admin/initDashboard")
}

export const initUserData = () => {
  return get("/admin/initUserData")
}

export const initConsultData = () => {
  return get("/admin/initConsultData")
}

export const initSystemData = () => {
  return get("/admin/initSystemData")
}
