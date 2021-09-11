import Cookies from 'js-cookie'

class Auth {
    static loginUser(token, remember) {
        remember ? Cookies.set('token', token, {
            expires: 30,
            sameSite: 'strict'
        }) : Cookies.set('token', token, {sameSite: 'strict'})
    }

    static logoutUser(token) {
        Cookies.remove('token')
    }

    static isAuthenticated() {
        return Cookies.get('token') !== undefined;
    }
}

export default Auth