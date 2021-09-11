import React from "react";
import Auth from "../utils/auth";
import {Link, Redirect} from "react-router-dom";

class UserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            redirect: null,
            email: null,
            emailError: null,
            password: null,
            passwordError: null,
            remember: false,
            action: this.props.action,
        }
        this.login = this.login.bind(this);
        this.register = this.register.bind(this);
        this.handleChange = this.handleChange.bind(this)
    }

    register(event) {
        event.preventDefault()
        const {email, password} = this.state
        const path = window.location.origin.replace('3000', '8000') + '/auth/users/'
        const data = JSON.stringify({email, password})
        fetch(path, {
            method: 'POST',
            mode: 'cors',
            body: data,
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                return new Promise((resolve) => response.json()
                    .then((json) => resolve({
                        status: response.status,
                        ok: response.ok,
                        json,
                    })));
            })
            .then(
                (result) => {
                    console.log(result)
                    if (result.ok) {
                        this.setState({redirect: '/login/', email: result.email})
                    } else {
                        this.setState({
                            error: result.json.non_field_errors,
                            emailError: result.json.email,
                            passwordError: result.json.password,
                            redirect: null
                        })
                    }
                },
                (error) => {
                    this.setState({error, emailError: error.email, passwordError: error.password, redirect: null})
                })
            .catch((error) => {
                this.setState({error, emailError: error.email, passwordError: error.password, redirect: null})
            })
    }

    login(event) {
        event.preventDefault()
        const {email, password} = this.state
        const path = window.location.origin.replace('3000', '8000') + '/auth/token/login'
        const data = JSON.stringify({email, password})
        fetch(path, {
            method: 'POST',
            mode: 'cors',
            body: data,
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                return new Promise((resolve) => response.json()
                    .then((json) => resolve({
                        status: response.status,
                        ok: response.ok,
                        json,
                    })));
            })
            .then(
                (result) => {
                    console.log(result)
                    if (result.ok) {
                        Auth.loginUser(result.token, this.state.remember)
                        this.setState({redirect: "/"})
                    } else {
                        this.setState({
                            error: result.json.non_field_errors,
                            emailError: result.json.email,
                            passwordError: result.json.password,
                            redirect: null
                        })
                    }

                },
                (error) => {
                    this.setState({error, emailError: error.email, passwordError: error.password, redirect: false})
                }
            )
            .catch((error) => {
                this.setState({error, emailError: error.email, passwordError: error.password, redirect: false})
            })
    }

    handleChange(event) {
        if (event.target.type === 'checkbox') {
            this.setState({remember: event.target.checked})
        } else {
            this.setState({[event.target.type]: event.target.value})
        }
    }

    render() {
        console.log(this.state)
        const caption = this.state.action === 'login' &&
            <p>Don't have account? <Link to={'/register/'}>Register here</Link>.</p>;
        if (this.state.redirect) {
            return <Redirect exact
                             push
                             to={this.state.redirect}/>
        } else {
            return (
                <form className={'user-form'}>
                    <p className={'form-title'}>{this.state.action === 'login' ? 'Login:' : 'Register:'}</p>
                    <div className={'email'}>
                        <div className={'input-border'}>
                            <input type={'email'}
                               placeholder={'Email...'}
                               onChange={this.handleChange}/>
                        </div>
                        {this.state.emailError && (<div>{this.state.emailError.map(message => <p>{message}</p>)}</div>)}
                    </div>
                    <div className={'password'}>
                        <div className={'input-border'}>
                            <input type={'password'}
                               placeholder={'Password...'}
                               onChange={this.handleChange}/>
                        </div>
                        {this.state.passwordError && (
                            <div>{this.state.passwordError.map(message => <p>{message}</p>)}</div>)}
                    </div>
                    <div className={'remember-me'}>
                        {this.state.action === 'login' && <label className={'checkbox-border'} htmlFor={'remember'}>Remember me:
                            <input id={'remember'}
                                                                 type={'checkbox'}
                                                                 onClick={this.handleChange}/>
                            <span className={'checkmark'}></span>
                        </label>}
                    </div>
                    <input type={'submit'}
                           className={'menu-item'}
                           value={this.state.action === 'login' ? 'Login' : 'Register'}
                           onClick={this.state.action === 'login' ? this.login : this.register}/>
                    {this.state.error && <div>{this.state.error.map(message => <p>{message}</p>)}</div>}
                    {caption}
                </form>
            )
        }
    }
}

export default UserForm
