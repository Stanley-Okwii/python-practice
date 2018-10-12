
class User {
    constructor(name) {
      this.name = name;
      this.lastLoggedInAt = null;
      this.loggedIn = false;
    }
    isLoggedIn() {
      return this.loggedIn;
    }
    getLastLoggedInAt() {
      return this.lastLoggedInAt;
    }
    logIn() {
      this.loggedIn = true;
      this.lastLoggedInAt = new Date();
    }
    logOut() {
      this.loggedIn = false;
    }
    getName() {
      return this.name;
    }
    setName(name) {
      this.name= name;
    }
    canEdit(comment) {
      if (comment.getAuthor().getName() === this.name) {
        return true;
      }
      return false;
    }
    canDelete(comment) {
      return false;
    }
  }
  
  class Moderator extends User {
    constructor(name) {
      super(name);
    }
    canDelete(comment) {
      return true;
    }
  }
  
  class Admin extends Moderator {
    constructor(name) {
      super(name);
    }
    canEdit(comment) {
      return true;
    }
  }
  
  class Comment {
    constructor(author, message, repliedTo) {
      this.createdAt = new Date();
      this.author = author;
      this.message = message;
      this.repliedTo = repliedTo || null;
    }
    getMessage() {
      return this.message;
    }
    setMessage(message) {
      this.message = message;
    }
    getCreatedAt() {
      return this.createdAt;
    }
    getAuthor() {
      return this.author;
    }
    getRepliedTo() {
      return this.repliedTo;
    }
    getString(comment) {
      const authorName = comment.getAuthor().getName();
      if (!comment.getRepliedTo()) return authorName;
      return `${comment.getMessage()} by ${authorName} (replied to ${this.getString(comment.getRepliedTo())})`;
    }
    toString() {
      const authorName = this.getAuthor().getName();
      if (!this.getRepliedTo()) {
        return `${this.message} by ${authorName}`;
      }
      return this.getString(this);
    }
  }
  