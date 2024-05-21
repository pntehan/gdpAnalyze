import { get, post } from "../utils/request"

export const getGDPData = query => {
  return get("/data/getGDPData", query)
}

export const addGDPData = query => {
  return post("/data/addGDPData", query)
}

export const editGDPData = query => {
  return post("/data/editGDPData", query)
}

export const predict = query => {
  return post("/data/predict", query)
}

export const login = query => {
  return post("/user/login", query)
}

export const register = query => {
  return post("/user/register", query)
}

export const updateUser = query => {
  return post("/user/updateUser", query)
}
