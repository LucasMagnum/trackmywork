package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewClearCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "clear",
      Short: "Clear all tasks",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Clear command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
