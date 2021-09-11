import Cookies from 'js-cookie'

class Auth {
    static loginUser(token, remember) {
        remember ? Cookies.set('authtoken', token, {
            expires: 30,
            sameSite: 'strict'
        }) : Cookies.set('authtoken', token, {sameSite: 'strict'})
    }

    static logoutUser() {
        Cookies.remove('authtoken')
    }

    static isAuthenticated() {
        return Cookies.get('authtoken') !== undefined;
    }

    static getToken() {
        return Cookies.get('authtoken')
    }
}

export default Auth