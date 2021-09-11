import React from "react";

class Thumbnail extends React.Component {
    render() {
        return (
            <div className={"image"}>
                <img src={this.props.image_url}  alt={"Product thumbnail"}/>
            </div>

        )
    }
}

export default Thumbnail